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
          label: "Temperature in C",
          data: temps,
          backgroundColor: 'orange'
        }  
        
      ]
    },
    options: {
      scales: {
          xAxes:[{
            scaleLabel: {
              display: true,
              labelString: 'DATE'
            }
          }],
          yAxes:[{
            scaleLabel: {
              display: true,
              labelString: 'TEMPERATURE'
            },
            ticks:{
              min: 0,
              max: 35,
              step: 2
            }
          }]
      }
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
    threshold[i]=JSON.stringify(data['Threshold'])
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
          backgroundColor: 'limegreen',
          fill:false
        },
        {
          label: "Threshold",
          data: threshold,
          borderColor: 'red',
          backgroundColor: 'magenta',
          fill:false
        }  
        
      ]
    },
    options: {
      scales: {
        xAxes:[{
          scaleLabel: {
            display: true,
            labelString: 'HITS'
          }
        }],
          yAxes:[{
            scaleLabel: {
              display: true,
              labelString: 'kWh'
            },
            ticks:{
              min: 0,
              max: 75,
              step: 0.5
            }
          }]
      }
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
        xAxes:[{
          scaleLabel: {
            display: true,
            labelString: 'DATES'
          }
        }],
          yAxes:[{
            scaleLabel: {
              display: true,
              labelString: 'kWh'
            },
            ticks:{
              min: 0,
              max: 100,
              step: 1
            }
          }]
      }
    }
    
  });
  console.log(dailyconsumption)
}


  


  
 