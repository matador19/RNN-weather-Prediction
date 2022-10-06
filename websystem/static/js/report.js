console.log(logs)
  new Chart("myChartA", {
    type: 'line', //this denotes tha type of chart

    data: {// values on X-Axis
      labels: ['2022-05-10', '2022-05-11', '2022-05-12','2022-05-13',
      '2022-05-14', '2022-05-15', '2022-05-16','2022-05-17',], 
       datasets: [
        {
          label: "Sales",
          data: ['467','576', '572', '79', '92',
               '574', '573', '576'],
          borderColor: 'blue',
          backgroundColor: 'blue',
          fill:false
        },
        {
          label: "Profit",
          data: ['542', '542', '536', '327', '17',
                 '0.00', '538', '541'],
          borderColor: 'limegreen',
          backgroundColor: 'limegreen',
          fill:false
        }  
        
      ]
    }
    
  });

  new Chart("myChartB", {
    type: 'bar', //this denotes tha type of chart

    data: {// values on X-Axis
      labels: ['2022-05-10', '2022-05-11', '2022-05-12','2022-05-13',
      '2022-05-14', '2022-05-15', '2022-05-16','2022-05-17',], 
       datasets: [
        {
          label: "Sales",
          data: ['467','576', '572', '79', '92',
               '574', '573', '576'],
          backgroundColor: 'black'
        },
        {
          label: "Profit",
          data: ['542', '542', '536', '327', '17',
                 '0.00', '538', '541'],
          backgroundColor: 'limegreen'
        }  
        
      ]
    }
    
  });

  new Chart("myChartC", {
    type: 'bar', //this denotes tha type of chart

    data: {// values on X-Axis
      labels: ['2022-05-10', '2022-05-11', '2022-05-12','2022-05-13',
      '2022-05-14', '2022-05-15', '2022-05-16','2022-05-17',], 
       datasets: [
        {
          label: "Sales",
          data: ['467','576', '572', '79', '92',
               '574', '573', '576'],
          borderColor: 'yellow',
          backgroundColor: 'yellow',
          fill:false
        },
        {
          label: "Profit",
          data: ['542', '542', '536', '327', '17',
                 '0.00', '538', '541'],
          borderColor: 'green',
          backgroundColor: 'green',
          fill:false
        }  
        
      ]
    }
    
  });

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
  
 