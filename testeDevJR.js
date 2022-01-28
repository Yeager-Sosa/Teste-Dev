// teste dev em JavaScript
var anagramaAgrupado = function (palavras) {
    
    const grupoAnagrama = {};

    for (let palavra of palavras) {

        const palavraOrdenada = palavra.split("").sort().join("");

        if (!grupoAnagrama[palavraOrdenada]) grupoAnagrama[palavraOrdenada] = [];

        grupoAnagrama[palavraOrdenada].push(palavra);
    }

    return Object.values(grupoAnagrama);
};

console.log(anagramaAgrupado(["nata", "sorvete", "anta", "paralelepipedo", "tana"]))