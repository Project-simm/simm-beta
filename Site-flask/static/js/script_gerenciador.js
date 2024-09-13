// Seleciona os campos de cadastro
const busca = document.getElementById('busca');
const data = document.getElementById('date');
const tempo = document.getElementById('time');
const quantidade = document.getElementById('qtd');
const btnRegistrar = document.getElementById('btnRegistrar');

// Adiciona um evento de click ao botão Registrar
btnRegistrar.addEventListener('click', (e) => {
  // Verifica se os campos estão preenchidos
  if (busca.value.trim() === '' || data.value.trim() === '' || tempo.value.trim() === '' || quantidade.value.trim() === '') {
    // Se algum campo estiver vazio, impede que o formulário seja submetido
    e.preventDefault();
    alert('Por favor, preencha todos os campos obrigatórios!');
  }
});