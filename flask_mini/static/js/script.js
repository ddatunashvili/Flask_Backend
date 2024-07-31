const dataForm = document.querySelector("#dataForm")

dataForm.addEventListener("submit",async (event) =>{
    event.preventDefault()
    const form = new FormData(dataForm)
    const jsonData = JSON.stringify(Object.fromEntries(form))

    const res = await fetch('/data', {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:jsonData
    })

    if (!res.ok){
        throw new Error("bad request")
    }
    const data = await res.json()
    console.log(data)

})