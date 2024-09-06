
//   ITEM - 12 -> PASTORAL (Mensagem)
  
  function adjustFontSize() {
    const div = document.getElementById('pastoral-content');
    let fontSize = 50; // Tamanho da fonte inicial
    let maxHeight = div.clientHeight;
    let maxWidth = div.clientWidth;

    while (div.scrollHeight > maxHeight || div.scrollWidth > maxWidth) {
      fontSize -= 0.5;
      div.style.fontSize = fontSize + 'px';
      if (fontSize <= 10) break; // Limite mínimo do tamanho da fonte
    }
  }

  window.addEventListener('load', adjustFontSize);
  window.addEventListener('resize', adjustFontSize);


//   ITEM - 8 -> CANAL DO YOUTUBE

const API_KEY = 'SUA_API_KEY_AQUI'; // Substitua pela sua chave de API do YouTube
const CHANNEL_ID = 'ID_DO_CANAL_AQUI'; // Substitua pelo ID do canal do YouTube

async function loadYouTubeLive() {
  const response = await fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=${CHANNEL_ID}&type=video&eventType=live&key=${API_KEY}`);
  const data = await response.json();
  
  if (data.items && data.items.length > 0) {
    const videoId = data.items[0].id.videoId;
    const iframe = document.createElement('iframe');
    iframe.width = '100%';
    iframe.height = '100%';
    iframe.src = `https://www.youtube.com/embed/${videoId}`;
    iframe.frameBorder = '0';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
    iframe.allowFullscreen = true;
    document.getElementById('youtube-live').appendChild(iframe);
  } else {
    document.getElementById('youtube-live').innerText = 'No live video currently.';
  }
}

window.addEventListener('load', loadYouTubeLive);


// PARTE DA TELA DE LOGIN
document.addEventListener('DOMContentLoaded', function() {
    
  // Adicione um listener de evento para o clique no ícone de exclusão
  document.querySelectorAll('.delete-icon').forEach(function(icon) {
      icon.addEventListener('click', function(e) {
          e.preventDefault();
          
          // Obtenha o ID do usuário a ser excluído do atributo data-id
          var usuarioId = this.getAttribute('data-id');
          console.log('Clicou no ícone de exclusão para o usuário com ID:', usuarioId); // Adicionando o log
         
          // Envie uma solicitação DELETE para a rota de exclusão
          fetch('/excluir/' + usuarioId, { method: 'DELETE' })
              .then(function(response) {

                  // Verifique se a exclusão foi bem-sucedida
                  if (response.ok) {
                      
                      // Redirecione o usuário para a página de conteúdo após a exclusão bem-sucedida
                      window.location.reload();
                      }
                  })
          .catch(function(error) {
              console.error('Erro ao excluir usuário:', error);
          });
      });
  });
});
