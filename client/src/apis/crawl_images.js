export function crawlImages (urls) {
    let form = new FormData();
    form.append('maximum', '100');
    form.append("urls", urls);
    let xhr = new XMLHttpRequest();
    let baseUrl = 'http://127.0.0.1:5000/';
    let url = '/api/crawlImages';
    xhr.open('POST', baseUrl + url, true);
    xhr.onload = function(){
        if (xhr.status === 200) {
            console.log(xhr.response);
            return xhr.response;
        } else {
            console.log('http error')
        }
    };
    xhr.send(form);

    // return request ({
    //         url: '/api/crawlImages',
    //         method: 'GET',
    //         baseUrl: 'http://127.0.0.1:5000/',
    //         params: params
    //     }
    // )
}