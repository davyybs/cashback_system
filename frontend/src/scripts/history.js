const url = "https://cashbacksystem-production.up.railway.app/cashback/history";

const answer = await fetch(url);
const data = await answer.json();

const tabel = document.getElementById("history");

tabel.innerHTML = data.map(function(item) {
    return `
        <tr>
            <td scope="col">R$${item.price}</td>
            <td scope="col">${item.vip ? "VIP" : "Comum"}</td>
            <td scope="col">R$${item.cashback_value.toFixed(2)}</td>
        </tr>
    `;
}).join("");