;

// Вывод динамической информации о пользователях(имя, фамилия, отчество, email, роль) в index.html шаблон
$(document).ready(function(){

    // Получение таблицы всех пользователей - начало

    function getAllWorkers() {
        var now = new Date();
        $.ajax({
            url: '/api/worker/?date_of_birth='+now.getFullYear()+'-'+(now.getMonth()+1)+'-'+now.getDate(),
            type: 'GET',
            success: function (response) {
                for (var i = 0; i < response.length; i++){
                    $('#table-body-workers').append(
                        '<tr id="' +  response[i].id + '">' +
                            '<th scope="row">' + response[i].id + '</th>' +
                            '<td class="first_name">' + response[i].first_name + '</td>' +
                            '<td class="last_name">' + response[i].last_name + '</td>' +
                            '<td class="middle_name">' + response[i].middle_name + '</td>' +
                            '<td class="email">' + response[i].email + '</td>' +
                            '<td class="role">' + response[i].role + '</td>' +
                            '<td><button class="worker-delete" data-id="' + response[i].id + '"> Удалить </button></td>' +
                            '<td><button class="worker-edit" data-id="' + response[i].id + '"> Редактировать </button></td>' +
                            '<td><button class="worker-lock" data-id="' + response[i].id + '"> Блокировать </button></td>' +
                        '</tr>'
                    );
                }
            },
            error: function(response) {
             alert(response.responseJSON.detail);
            }
        });
    }

    getAllWorkers();

    // Получение таблицы всех пользователей - начало

    // Удаление пользователя из таблицы - начало

    function deleteWorker(id) {
        $.ajax({
            url: '/api/worker/' + id + '/',
            type: 'DELETE',
            success: function () {
                $('#' + id).remove();
            },
            error: function(response) {
             alert(response.responseJSON.detail);
            }
        })
    }
    $(document).on('click', '.worker-delete', function(){
        // this - javascript
        // $(this) - jquery
        var $this = $(this);
        var idWorker = $this.attr('data-id');
        deleteWorker(idWorker);
    });

    // Удаление пользователя из таблицы - конец

    // Редактирование пользователя - начало

    function getWorker(id) {
        $.ajax({
            url: '/api/worker/' + id + '/',
            type: 'GET',
            async: false,
            success: function (response) {
                $('#myModal').find('[name="first_name"]').val(response.first_name);
                $('#myModal').find('[name="last_name"]').val(response.last_name);
                $('#myModal').find('[name="middle_name"]').val(response.middle_name);
                $('#myModal').find('[name="email"]').val(response.email);
                $('#myModal').find('[name="role"]').val(response.role);
                $('#myModal').attr('data-id', response.id);
                $('#myModal').modal('show');
            },
            error: function(response) {
             alert(response.responseJSON.detail);
            }
        })
    }
    $(document).on('click', '.worker-edit', function(){
        // this - javascript
        // $(this) - jquery
        var $this = $(this);
        var idWorker = $this.attr('data-id');
        getWorker(idWorker);
    });

    // Редактирование пользователя - конец

    // Сохранение изменений пользователя - начало

    function saveWorker(id) {
        $.ajax({
            url: '/api/worker/' + id + '/',
            type: 'PUT',
            data: $('#formOutput').serialize(),
            async: false,
            success: function (response) {
                $('#table-body-workers').find('#' + id).find('.first_name').text(response.first_name);
                $('#table-body-workers').find('#' + id).find('.last_name').text(response.last_name);
                $('#table-body-workers').find('#' + id).find('.middle_name').text(response.middle_name);
                $('#table-body-workers').find('#' + id).find('.email').text(response.email);
                $('#table-body-workers').find('#' + id).find('.role').text(response.role);
                $('#myModal').modal('hide');
            },
            error: function(response) {
                if ({}.hasOwnProperty.call(response.responseJSON, 'detail')) {
                    alert(response.responseJSON.detail);
                } else {
                    alert(response.responseText);
                }
            }
        })
    }
    $(document).on('click', '.worker-save', function(){
        // this - javascript
        // $(this) - jquery
        var $this = $(this);
        var idWorker = $('#myModal').attr('data-id');
        saveWorker(idWorker);
    });

    // Сохранение изменений пользователя - начало

    // Блокировка пользователя - начало

    function patchWorker(id) {
        $.ajax({
            url: '/api/worker/' + id + '/',
            type: 'PATCH',
            data: 'is_active=false',
            async: false,
            success: function (response) {

            },
            error: function(response) {
             alert(response.responseJSON.detail);
            }
        })
    }
    $(document).on('click', '.worker-lock', function(){
        // this - javascript
        // $(this) - jquery
        var $this = $(this);
        var idWorker = $this.attr('data-id');
        patchWorker(idWorker);
    });

    // Блокировка пользователя - конец

});

