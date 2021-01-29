    $('#CurrUsers').on('click', function(){
        console.log('congrats you did it')
        $.ajax({url:'/users', success:function(response){
            $('.servRes').html(response)
        } 
            
        })
    });
    





// $(function ($){
//     console.log($.ajax);
// });