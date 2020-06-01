from nameko.rpc import rpc

import dependencies, schemas
import pymysql
class BreweryService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'book_service'

    # ==========================================================
    # ----------------------- Dependency -----------------------
    # ==========================================================

    database = dependencies.Database()

    # ==========================================================
    # ------------------------ Functions -----------------------
    # ==========================================================

    def __init__(self):
        print("Service Constructor")

    @rpc
    def get_all_book(self):
        brewery = self.database.get_all_book()
        self.database.close_connection()
        return schemas.BookSchema(many=True).dump(brewery)
    
    @rpc
    def get_book_by_id(self, id):
        brewery = self.database.get_book_by_id(id)
        self.database.close_connection()
        return schemas.BookSchema().dump(brewery)
    
    @rpc
    def update_status(self, id, review):
        self.database.update_status(id, review)

    def __del__(self):
        print("Service Destructor")