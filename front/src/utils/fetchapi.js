const BASEURL = "http://54.232.165.147:8000";

async function getApi(url){
    const fullUrl = BASEURL + url;
    try {
        const response = await fetch(fullUrl);
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
    const fullUrl = BASEURL + url;
    try {
        const response = await fetch(fullUrl, {
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

export async function getAuthApi(url, token){
    const fullUrl = BASEURL + url;
    try {
        const response = await fetch(fullUrl, {
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

export async function postAuthApi(url, data, token){
    const fullUrl = BASEURL + url;
    try {
        const response = await fetch(fullUrl, {
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
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