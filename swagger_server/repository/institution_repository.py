import connexion
import json
from swagger_server.models.request_institution_add import RequestInstitutionAdd
sql_select = "select * from institution where status = 'A'"

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def add_institution(self, body):
        if connexion.request.is_json:
            body = RequestInstitutionAdd.from_dict(connexion.request.get_json())
            #Transformo las variables con dumps a string para que puedan ser leidas en el insert y no las detecte como json
            name = json.dumps(body.name)
            description = json.dumps(body.description)
            address = json.dumps(body.address)
            created_user = json.dumps(body.created_user)

            with self.session_factory() as session:
                sql_insert = f"INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) select max(id)+1 id, {name}, {description}, {address}, {created_user}, now(), NULL, NULL, 'A' from institution"
                session.execute(sql_insert)
                session.commit()
                return 'Insertado Exitoso'

    def get_institution_by_id(self, institution_id):
        with self.session_factory() as session:
            sql_busqueda = f"select * from institution where id = {institution_id}"
            rows = session.execute(sql_busqueda)
            return rows
