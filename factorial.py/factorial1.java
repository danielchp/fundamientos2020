consola . log ( "Hola Mundo !!!!!" ) ;
var  contenido = "" ;
función  calcularFactorial ( numero ) {
    var  contador = 1 ;
    var  resultado = 1 ;
    if  ( numero == 0 ) {
        resultado = 1 ;
    } más {
        resultado = numero ;
    }    
    while  ( contador < numero ) {        
        resultado = resultado * contador ;
        contador = contador + 1 ;
    }
    consola . log ( "El factorial de" + numero + "es" + resultado ) ;
    
}

function  calcularFactorialBig ( numero )  {
    var  contador = 1 ;
    var  resultado = BigInt ( 1 ) ;
    if ( numero > 1 ) { resultado = BigInt ( numero ) ; }
    while ( contador < numero ) {
        resultado = resultado * BigInt ( contador ) ;
        contador ++ ;
    }
    consola . log ( "El factorial de" + numero + "es" + resultado ) ;

    return  "El factorial de" + numero + "es" + resultado + "<br/>" ;
}


function  rangoFactorial ( numfinal )  {
    for ( var  inicio = 0 ; inicio <= numfinal ; inicio ++ ) {
       contenido = contenido +  calcularFactorialBig ( inicio ) ;
    }
    documento . getElementById ( "demostración" ) . innerHTML  = contenido ;
}

rangoFactorial ( 1000 )