async function fetchAPI(endpoint, method, body) {
  try {
    console.log(__myapp);
    const api_url = __myapp.env.isProd
      ? __myapp.env.API_URL
      : __myapp.env.LOCAL_API;
    const url = `${api_url}${endpoint}`;

    let httpResponse = await fetch(url, {
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
