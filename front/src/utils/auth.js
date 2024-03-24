import { getAuthApi } from "./fetchapi.js";

export async function checkJwtTokenIsValid(token){
    const url = "/auth/v1/user";
    const userData = await getAuthApi(url, token);
    return userData
}

export function getToken(){
    const jwtToken = localStorage.getItem('jwt');
    return jwtToken
}