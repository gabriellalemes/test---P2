def buscar_usuario(usuario_id):
    return{
        "id": usuario_id,
        "nome": "Zoe Isabel"
    }

def obter_nome(usuario_id):
    usuario = buscar_usuario(usuario_id)
    return usuario["nome"]

