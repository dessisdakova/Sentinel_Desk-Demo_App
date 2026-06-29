from dataclasses import dataclass

import psycopg2.extensions


@dataclass(frozen=True)
class ColumnInfo:
    """One column row from information_schema.columns."""

    name: str
    data_type: str       # e.g. "character varying", "uuid"
    udt_name: str        # e.g. "varchar", "user_role", "timestamptz"
    is_nullable: str     # "YES" or "NO" — same as information_schema


class PostgresInspector:
    """Read-only schema introspection for integration tests."""

    def __init__(self, connection: psycopg2.extensions.connection) -> None:
        self._conn = connection

    def _fetchall(self, sql: str, params: tuple = ()) -> list[tuple]:
        """Run a query and return all rows. Private — tests never call this."""
        with self._conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

    def _fetchone(self, sql: str, params: tuple = ()) -> tuple | None:
        with self._conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()
    
    def get_columns(
        self,
        table: str,
        *,
        schema: str = "public",
    ) -> list[ColumnInfo]:
        """Return columns in ordinal order."""
        rows = self._fetchall(
            """
            SELECT column_name, data_type, udt_name, is_nullable
            FROM information_schema.columns
            WHERE table_schema = %s AND table_name = %s
            ORDER BY ordinal_position
            """,
            (schema, table),
        )
        return [
            ColumnInfo(name=r[0], data_type=r[1], udt_name=r[2], is_nullable=r[3])
            for r in rows
        ]

    def get_column_map(
        self,
        table: str,
        *,
        schema: str = "public",
    ) -> dict[str, ColumnInfo]:
        """Same as get_columns, keyed by column name — handy for users table tests."""
        return {col.name: col for col in self.get_columns(table, schema=schema)}
    
    def get_primary_key_columns(
        self,
        table: str,
        *,
        schema: str = "public",
    ) -> list[str]:
        rows = self._fetchall(
            """
            SELECT kcu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
              ON tc.constraint_schema = kcu.constraint_schema
             AND tc.constraint_name = kcu.constraint_name
            WHERE tc.table_schema = %s
              AND tc.table_name = %s
              AND tc.constraint_type = 'PRIMARY KEY'
            ORDER BY kcu.ordinal_position
            """,
            (schema, table),
        )
        return [row[0] for row in rows]

    def get_foreign_keys(
        self,
        table: str,
        *,
        schema: str = "public",
    ) -> list[tuple[str, str, str]]:
        rows = self._fetchall(
            """
            SELECT kcu.column_name, ccu.table_name, ccu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
              ON tc.constraint_name = kcu.constraint_name
             AND tc.table_schema = kcu.table_schema
             AND tc.table_name = kcu.table_name
            JOIN information_schema.constraint_column_usage ccu
              ON tc.constraint_name = ccu.constraint_name
             AND tc.table_schema = ccu.table_schema
            WHERE tc.table_schema = %s
              AND tc.table_name = %s
              AND tc.constraint_type = 'FOREIGN KEY'
            ORDER BY kcu.column_name
            """,
            (schema, table),
        )
        return [(r[0], r[1], r[2]) for r in rows]

    def get_indexes(
        self,
        table: str,
        *,
        schema: str = "public",
    ) -> dict[str, str]:
        """index_name -> indexdef (from pg_indexes)."""
        rows = self._fetchall(
            """
            SELECT indexname, indexdef
            FROM pg_indexes
            WHERE schemaname = %s AND tablename = %s
            """,
            (schema, table),
        )
        return {row[0]: row[1] for row in rows}

    def get_enum_labels(self, enum_name: str) -> tuple[str, ...]:
        rows = self._fetchall(
            """
            SELECT e.enumlabel
            FROM pg_type t
            JOIN pg_enum e ON t.oid = e.enumtypid
            WHERE t.typname = %s
            ORDER BY e.enumsortorder
            """,
            (enum_name,),
        )
        return tuple(row[0] for row in rows)

    def get_alembic_revision(self) -> str | None:
        row = self._fetchone("SELECT version_num FROM alembic_version")
        return None if row is None else row[0]