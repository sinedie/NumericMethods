async function fetchAPI(url, method, body) {
  try {
    let httpResponse = await fetch(`http://localhost:5000/api${url}`, {
      method,
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    return httpResponse;
  } catch (e) {
    console.log(e);
  }
}

async function graficar(func, xi, xf) {
  const httpResponseImage = await fetchAPI("/raices/grafico", "POST", {
    func,
    xi,
    xf,
  });
  const image = await httpResponseImage.json();
  return image;
}

async function solve_function(method, body) {
  try {
    const httpResponse = await fetchAPI(`/raices/${method}`, "POST", body);
    let response = await httpResponse.json();
    return response;
  } catch (e) {
    console.log(e);
  }
}

export { fetchAPI, solve_function, graficar };
