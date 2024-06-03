

import data from './columns.json' assert {type : 'json'};
console.log(data.data_columns)
const locations=document.querySelector('.location');
    for(let i=3;i<243;i++){
        let newoption=document.createElement("option")
        newoption.innerText=data.data_columns[i];
        newoption.value=data.data_columns[i];
        locations.append(newoption);
     }


