from nameko.rpc import rpc

import dependencies, schemas
import pymysql
class BreweryService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'user_service'

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
    def get_all_user(self):
        brewery = self.database.get_all_user()
        self.database.close_connection()
        return schemas.UserSchema(many=True).dump(brewery)
    
    @rpc
    def get_user_by_id(self, id):
        brewery = self.database.get_user_by_id(id)
        self.database.close_connection()
        return schemas.UserSchema().dump(brewery)
    
    @rpc
    def ban_user(self, id, review):
        self.database.ban_user(id, review)

    @rpc
    def verify_user(self, id):
        brewery = self.database.get_user_by_id(id)
        self.database.close_connection()
        return brewery['status'] == 'ACTIVE'

    def __del__(self):
        print("Service Destructor")