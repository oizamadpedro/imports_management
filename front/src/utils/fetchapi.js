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

export async function getAuthApi(url, token){
    try {
        const response = await fetch(url, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });
        if (!response.ok) {
        throw new Error(`Erro na requisição: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Erro ao buscar dados:", error);
        // Trate o erro, se necessário
    }
}

async function postApi(url, data){
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const responseData = await response.json();
        return responseData;
    } catch (error) {
        console.error("Erro ao fazer requisição:", error);
        // Trate o erro, se necessário
    }
}

export {
    getApi,
    postApi
}