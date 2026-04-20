export function saveSession(data){
        localStorage.setItem("session",JSON.stringify(data));
}

export function getSession(){
    return JSON.parse(localStorage.getItem("session"));
}

export function clearSession(){
    localStorage.removeItem("session");
}

