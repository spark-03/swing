const SUPABASE_URL = "YOUR_SUPABASE_URL";
const SUPABASE_ANON_KEY = "YOUR_SUPABASE_ANON_KEY";

async function loadPrice() {

    const response = await fetch(
        `${SUPABASE_URL}/rest/v1/stock_prices?select=*&symbol=eq.RELIANCE&order=created_at.desc&limit=1`,
        {
            headers: {
                apikey: SUPABASE_ANON_KEY,
                Authorization: `Bearer ${SUPABASE_ANON_KEY}`
            }
        }
    );

    const data = await response.json();

    if (data.length > 0) {

        document.getElementById("price").innerText =
            "₹" + data[0].price;

        document.getElementById("updated").innerText =
            "Last Updated: " +
            new Date(data[0].created_at).toLocaleString();
    }
}

loadPrice();

setInterval(loadPrice, 30000);
