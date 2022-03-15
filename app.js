<<<<<<< HEAD
const btnGpio = document.getElementById('btn-gpio')
const btnUart = document.getElementById('btn-uart')
const btnSensors = document.getElementById('btn-sensors')

const gpio = document.getElementById('gpio')
const uart = document.getElementById('uart')
const sensors = document.getElementById('sensors')

btnGpio.addEventListener('click', function(){
    gpio.classList.remove('hide')
    uart.classList.add('hide')
<<<<<<< HEAD
    sensors.classList.add('hide')

    btnGpio.classList.add('pressed')
    btnUart.classList.remove('pressed')
    btnSensors.classList.remove('pressed')
})

btnUart.addEventListener('click', function(){
    uart.classList.remove('hide')
    gpio.classList.add('hide')
    sensors.classList.add('hide')

    btnUart.classList.add('pressed')
    btnGpio.classList.remove('pressed')
    btnSensors.classList.remove('pressed')
})

btnSensors.addEventListener('click', function(){
    sensors.classList.remove('hide')
    gpio.classList.add('hide')
    uart.classList.add('hide')

    btnSensors.classList.add('pressed')
    btnGpio.classList.remove('pressed')
    btnUart.classList.remove('pressed')
=======
=======
const btnGpio = document.getElementById('btn-gpio')
const gpio = document.getElementById('gpio')
const uart = document.getElementById('uart')
const sensors = document.getElementById('sensors')

btnGpio.addEventListener('click', function(){
    uart.classList.add('hide')
>>>>>>> 981ba05cce32bdb29c596cf715e379adcaa75a7c
>>>>>>> 1c425d9fe90530548aa4fa88dd9d15cdd47a2ebb
})