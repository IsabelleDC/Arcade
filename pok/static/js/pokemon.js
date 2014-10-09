
$(document).ready(function()
{
    pokeContainer = $('#pokeContainer');
    $('#randomPokemon').on('click', function () {
    var num = Math.floor(Math.random() * (719 - 2) + 2);
        var pokemon = {};
        $.ajax({
            url: "http://pokeapi.co/api/v1/sprite/" + num,
            dataType: "jsonp",
            type: "GET",
            success: function (data) {

                pokemon.team = 2;
                pokemon.name = data.name.split('_')[0];
                pokemon.pokedex_id = data.id - 1;
                pokemon.image = 'http://pokeapi.co/' + data.image;

                pokeContainer.children().remove();
                pokeContainer.append("<img class='pokemon' src='" + pokemon.image + "'/>");
                pokeContainer.append('<button id="savePokemon" class="btn btn-info">Save me!</button>');


                $('#savePokemon').on('click', function () {
                    var pokeInfo = JSON.stringify(pokemon);
                    $.ajax({
                        url: '/new_pokemon/',
                        dataType: 'json',
                        data: pokeInfo,
                        type: "POST",
                        success: function (data) {
                            console.log('success');
                        },
                        error: function (data) {
                            console.log(data);
                        }
                    })
                })


            }
        });
    });

        $('#getTeam').on('click', function () {
//            alert('tests!!!!!!!');
            $("#teamContainer").html("");
            var pokemonTeam = [];
            var teamName="";
            var teamNumber = Math.floor(Math.random()*1000);
            teamContainer = $('#teamContainer');
            for (var j = 0; j < 6; j++) {
                var num = Math.floor(Math.random() * (719 - 2) + 2);
                $.ajax({
                    url: "http://pokeapi.co/api/v1/sprite/" + num,
                    dataType: "jsonp",
                    type: "GET",
                    success: function(data) {
                        var pokemon = {};
                        pokemon.team = teamNumber;
                        pokemon.name = data.name.split('_')[0];
                        pokemon.pokedex_id = data.id - 1;
                        pokemon.image = 'http://pokeapi.co/' + data.image;

                        // Append the pokemon to the team
                        pokemonTeam.push(pokemon);

                        teamContainer.append("<img class='pokemon' src='" + pokemon.image + "'/>");
                        console.log(pokemonTeam);

                        if (pokemonTeam.length == 6) {

                            teamContainer.append('Team name: <input type="text" name="teamname"><br><button id="saveTeamName" class="btn btn-info">Save the team name!</button><button id="saveTeam" class="btn btn-info">Save the team!</button>');
                            $('#saveTeamName').on('click', function () {
//                                    console.log(JSON.stringify();

                                    $.ajax({
                                        url: "/new_team/",
                                        dataType: "json",
                                        data: JSON.stringify({'name': $('[name=teamname]').val()}),
                                        type: "POST",
                                        success: function(data){
                                            teamName = data[0].pk;
                                            console.log(data[0].fields.name);//.fields.pk);
                                        }
                                    })

                            });
                            $('#saveTeam').on('click', function () {

                                for (var i = 0; i < pokemonTeam.length; i++) {
                                    pokemonTeam[i].team = teamName;
                                    console.log(JSON.stringify(pokemonTeam[i]));

                                    //console.log(JSON.stringify(pokemonTeam[i]));
                                    $.ajax({
                                        url: "/new_pokemon/",
                                        dataType: "json",
                                        data: JSON.stringify(pokemonTeam[i]),
                                        type: "POST",
                                        success: function(data){
                                            console.log('success!');
                                        }
                                    })
                                }
                            });
                        }


                    }
                })
            }
    });
});


