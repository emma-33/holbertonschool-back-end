export default function returnHowManyArguments(...Args) {
    let total = 0;
    for (const arg of Args){
        total += 1;
    }
    return total;
}
