from ariadne.asgi import GraphQL
from ariadne import ObjectType, load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, MutationType, QueryType
from .models import users_resolver
from db.repository import UserService, SQLRepository

repository = SQLRepository(connection_uri="mongodb://root:12345678@127.0.0.1:27017/",db_name="database",table_name="persons")
userService  = UserService(repository=repository)

query = QueryType()
mutation = MutationType()


@query.field("get_all_users")
def resolve_all_users(*_):
    return users_resolver()

@query.field("get_user_by_id")
def resolve_get_user_by_id(*_, id):
    user = userService.get_user_by_id(id)
    return user

@mutation.field("add_user")
def resolve_add_user(_, info, user_details):
    userService.create_user(user_details)
    user_details["id"] = str(user_details.pop("_id"))
    return user_details

@mutation.field("update_user")
def resolve_update_user(_, info, user_details):
    updated_user = userService.update_user(user_details)
    return updated_user

@mutation.field("delete_user")
def resolve_delete_user(_, info, id):
    userService.delete_user(id)
    return True

schema_str = load_schema_from_path("schema.graphql")
schema = make_executable_schema(schema_str, [query, mutation], convert_names_case=snake_case_fallback_resolvers)

app = GraphQL(schema, debug=True)
