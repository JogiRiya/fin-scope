document.getElementById("financeForm").addEventListener("submit", async function(e) {
  e.preventDefault();
  const income = document.getElementById("income").value;
  const expenses = document.getElementById("expenses").value;

  const res = await fetch("https://your-backend-url.onrender.com/api/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ income, expenses })
  });

  const data = await res.json();
  document.getElementById("result").innerText = data.message;
});

