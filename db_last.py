from database import CursorFromConnectionPool


class Content:
    def __init__(self, name, revenue, timestamp):
        self.name = name
        self.revenue = revenue
        self.timestamp = timestamp

    @classmethod
    def load(cls, name):
        with CursorFromConnectionPool() as cursor:
            sql = """ 

            SELECT "Name","TotalRevenue","RecordDate" FROM "ContentItemData" CI
            JOIN "PillarItems" PI
            ON
            CI."PillarItemId" = PI."Id"
            WHERE "Name" = %s

                """
            cursor.execute(sql, (name,))
            data = cursor.fetchall()
            from_db = []
            for i in data:
                from_db.append(i)

            return from_db

