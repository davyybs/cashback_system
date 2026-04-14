import 'bootstrap/dist/js/bootstrap.bundle.min.js';

document.getElementById("cashbackForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const price = document.getElementById("price").value;
    const discount = document.getElementById("discount").value || 0;
    const vip = document.getElementById("vip").value;
    
    const url = `http://localhost:8000/cashback/?price=${price}&discount=${discount}&vip=${vip}`;
    
    const answer = await fetch(url);
    const data = await answer.json();
    
    document.getElementById("result").innerText= `Valor do Cashback: R$${data.cashback_value}`;
});
