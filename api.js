
const verContato = document.getElementById('verContato');

var loadContatos = ()=>{

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

};
loadContatos();


var addCc = ()=>{
    
};


var openContato = (id)=>{

    var lista = verContato.querySelector('ul');
    lista.innerHTML = ''

    fetch('http://127.0.0.1:5000/contato/' + id)
      .then(resp => resp.json())
      .then(resp =>{
        resp.forEach(contato => {
          lista.innerHTML += `
          
          <li id="contN${contato.id}">

              <div class="div-flex" style="gap: 20px;">
                  <i class="bi bi-${contato.tipo}"></i>
                  <input class="valor" value="${contato.contato}" disabled>
              </div>

              <div class="div-flex" style="gap: 20px;">
                  <i onclick="alert()" class="bi bi-pencil"></i>
                  <i onclick="deletContato(${contato.id})" class="bi bi-trash"></i>
              </div>

          </li>
          
          `
        })
      });
    
    verContato.showModal();
};


var deletContato = (id) =>{

    fetch(`http://127.0.0.1:5000/del_cc/${id}`,{
        method: 'DELETE',
    })
    .then(resp => resp.json())
    .then(resp => {
        openContato(resp.id_contato)
    })
}


