let url = '/weatherAPI';
fetch(url)
.then(
  response =>{
  results=response.json()
  return results;
})
.then(weathertemps)
function weathertemps(data){
  temps=[];
  dates=[];
  for(i in data){
    dates[i]=JSON.stringify(data[i].CreationDate)
    temps[i]=+String(data[i].Temperature)
  }
  console.log(dates)
  new Chart("myChartB", {
    type: 'bar', //this denotes tha type of chart

    data: {// values on X-Axis
      labels: dates, 
       datasets: [
        {
          label: "Temperature",
          data: temps,
          backgroundColor: 'limegreen'
        }  
        
      ]
    }
    
  });


}

fetch('/powerinputinten')
.then(
  response =>{
  results=response.json()
  return results;
})
.then(powerconsumed)

function powerconsumed(data){
  var currentdate = new Date()
  count=[];
  kWh=[];
  threshold=[];
  dailyconsumption=[]
  dates=[]
  for(i in data['power consumed today']){
    kWh[i]=JSON.stringify(data['power consumed today'][i])
    count[i]=i
    //set for now
    threshold[i]=10
  }

  for(i in data['power consumed daily']){
    dailyconsumption[i]=String(Object.values(data['power consumed daily'][i]))
    dates[i]=Object.keys(data['power consumed daily'][i])
  }


  new Chart("myChartA", {
    type: 'line', //this denotes tha type of chart

    data: {// values on X-Axis
      labels: count, 
       datasets: [
        {
          label: "Consumption",
          data: kWh,
          borderColor: 'blue',
          backgroundColor: 'blue',
          fill:false
        },
        {
          label: "Threshold",
          data: threshold,
          borderColor: 'limegreen',
          backgroundColor: 'limegreen',
          fill:false
        }  
        
      ]
    }
    
  });


  
  new Chart("myChartC", {
    type: 'bar', //this denotes tha type of chart

    data: {// values on X-Axis
      labels: dates, 
       datasets: [
        {
          label: "Daily consumption",
          data: dailyconsumption,
          borderColor: 'purple',
          backgroundColor: 'purple',
          fill:false
        }
        
      ]
    },
    options: {
      scales: {
          yAxes:[{
            ticks:{
              Min: 0,
              max: 100,
              step: 1
            }
          }]
      }
    }
    
  });
  console.log(dailyconsumption)
}


  



  new Chart("myChartD", {
    type: 'line', //this denotes tha type of chart

    data: {// values on X-Axis
      labels: ['2022-05-10', '2022-05-11', '2022-05-12','2022-05-13',
      '2022-05-14', '2022-05-15', '2022-05-16','2022-05-17',], 
       datasets: [
        {
          label: "Sales",
          data: ['467','576', '572', '79', '92',
               '574', '573', '576'],
          borderColor: 'red',
          backgroundColor: 'red',
          fill:false
        },
        {
          label: "Profit",
          data: ['542', '542', '536', '327', '17',
                 '0.00', '538', '541'],
          borderColor: 'blue',
          backgroundColor: 'blue',
          fill:false
        }  
        
      ]
    }
    
  });
  
 