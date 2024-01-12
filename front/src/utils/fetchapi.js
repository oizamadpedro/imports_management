async function getApi(url){
    try {
        const response = await fetch(url);
        if (!response.ok) {
        throw new Error(`Erro na requisição: ${response.status}`);
        }
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error("Erro ao buscar dados:", error);
        // Trate o erro, se necessário
    }
}

async function postApi(url, data){
    fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json',
        },
    })
    .then((resp) => resp.json())
    .catch((err) => {
        console.log(err)
    })
}

export {
    getApi,
    postApi
}