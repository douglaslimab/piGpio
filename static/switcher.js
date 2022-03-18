const switcher_box_1 = document.getElementById('switcher-box-1')
const switcher_box_2 = document.getElementById('switcher-box-2')
const switcher_box_3 = document.getElementById('switcher-box-3')
const switcher_box_4 = document.getElementById('switcher-box-4')
const switcher_box_5 = document.getElementById('switcher-box-5')
const switcher_box_6 = document.getElementById('switcher-box-6')
const switcher_box_7 = document.getElementById('switcher-box-7')
const switcher_box_8 = document.getElementById('switcher-box-8')
const switcher_box_9 = document.getElementById('switcher-box-9')
const switcher_1 = document.getElementById('switcher-1')
const switcher_2 = document.getElementById('switcher-2')
const switcher_3 = document.getElementById('switcher-3')
const switcher_4 = document.getElementById('switcher-4')
const switcher_5 = document.getElementById('switcher-5')
const switcher_6 = document.getElementById('switcher-6')
const switcher_7 = document.getElementById('switcher-7')
const switcher_8 = document.getElementById('switcher-8')
const switcher_9 = document.getElementById('switcher-9')


switcher_box_1.addEventListener('click', function(){
    switcher_box_1.classList.toggle('tog-on')
    switcher_1.classList.toggle('on-off')

    if (switcher_box_1.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay1/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay1/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})

switcher_box_2.addEventListener('click', function(){
    switcher_box_2.classList.toggle('tog-on')
    switcher_2.classList.toggle('on-off')

    if (switcher_box_2.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay2/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay2/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})

switcher_box_3.addEventListener('click', function(){
    switcher_box_3.classList.toggle('tog-on')
    switcher_3.classList.toggle('on-off')

    if (switcher_box_3.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay3/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay3/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})
switcher_box_4.addEventListener('click', function(){
    switcher_box_4.classList.toggle('tog-on')
    switcher_4.classList.toggle('on-off')


    if (switcher_box_4.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay4/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay4/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})

switcher_box_5.addEventListener('click', function(){
    switcher_box_5.classList.toggle('tog-on')
    switcher_5.classList.toggle('on-off')

    if (switcher_box_5.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay5/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay5/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})

switcher_box_6.addEventListener('click', function(){
    switcher_box_6.classList.toggle('tog-on')
    switcher_6.classList.toggle('on-off')

    if (switcher_box_6.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay6/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay6/off'
    }
    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})

switcher_box_7.addEventListener('click', function(){
    switcher_box_7.classList.toggle('tog-on')
    switcher_7.classList.toggle('on-off')

    if (switcher_box_7.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay7/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay7/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})

switcher_box_8.addEventListener('click', function(){
    switcher_box_8.classList.toggle('tog-on')
    switcher_8.classList.toggle('on-off')

    if (switcher_box_8.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay8/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay8/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})

switcher_box_9.addEventListener('click', function(){
    switcher_box_9.classList.toggle('tog-on')
    switcher_9.classList.toggle('on-off')

    if (switcher_box_9.classList.contains('tog-on')){
      url = 'http://dougserver:8000/gpio/relay9/on'
    } else{
      url = 'http://dougserver:8000/gpio/relay9/off'
    }

    fetch(url).then(function(res){
      return response.json()
    }).then(function(data){
      console.log(data)
    }).catch(function(){
      console.log(err)
    })
})
