async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        console.log(error)
        error.response = response;
        throw error;
    }
}
async function buttonClick(event){
        let url = event.target.dataset.indexLink;
        let pk = event.target.dataset.id
        let div = document.getElementById(`div-${pk}`)
        div.removeChild(div.firstElementChild)
        console.log('url ', url)
        let response = await makeRequest(url);
        console.log('response ', response)
        if(response.status === false){
            console.log('403');
        } else if(response.status === true){
            console.log('200 ok');
        }
    }



async function buttonClickCancel(event){
        let url = event.target.dataset.indexLink;
        let pk = event.target.dataset.id
        let div = document.getElementById(`div-${pk}`)
        div.removeChild(div.firstElementChild)
        console.log('url ', url)
        let response = await makeRequest(url);
        console.log('response ', response)
        if(response.status === false){
            console.log('403');
        } else if(response.status === true){
            console.log('200 ok');
        }
    }
