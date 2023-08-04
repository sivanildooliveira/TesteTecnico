

fetch('http://127.0.0.1:5000/lista')
    .then(resp => resp.json())
    .then(resp => {
        const lista = document.getElementById('listaContatosInit');
        lista.innerHTML = ''

        resp.forEach(contato => {
            lista.innerHTML += `
            <tr ondblclick="openContato(${contato.id})">
                <td class="nome-tb"><h4>${contato.nome}</h4><small>${contato.contatos} contatos salvos</small></td>
            </tr>`
        });
    })