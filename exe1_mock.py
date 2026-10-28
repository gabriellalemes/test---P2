def obter_nome(usuario_id):
    result = buscar_nome(usuario_id)
    return result


def buscar_nome(usuario_id):
    return{
        "id": usuario_id,
        "nome": "Zoe Isabel"
    }