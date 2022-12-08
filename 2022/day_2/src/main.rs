use std::fs;
use std::collections::HashMap;

fn read_input_data() -> String {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    return data;
}

fn part_one(split_data: &Vec<&str>) {

    // Mapping of win conditions from player perspective
    let game_key = HashMap::from([
        ("X", "C"),
        ("Y", "A"),
        ("Z", "B")
    ]);
    
    // Mapping of player equivelant of opponent moves
    let identical_move_key = HashMap::from([
        ("A", "X"),
        ("B", "Y"),
        ("C", "Z")
    ]);
    
    // Mapping of value for moves to be applied to player score
    let move_values = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3),
    ]);

    let win_points = 6;
    let draw_points = 3;

    let mut player_score = 0;
   
    for raw_pair in split_data {
        
        // Split each data point into a Vector of [opponent_move, player_move]
        let pair: Vec<&str> = raw_pair.split(" ").collect::<Vec<&str>>();

        let opponent_move = pair[0];
        let player_move = pair[1];

        // Player move beats opponent move
        if game_key[player_move] == opponent_move {
            player_score += win_points;
        }
        // Player move is the relative identical move to opponent
        else if identical_move_key[opponent_move] == player_move {
            player_score += draw_points;
        }
        player_score += move_values[player_move];
    }

    println!("{}", player_score);
}

fn part_two(split_data: &Vec<&str>) {

    // Mapping of win conditions from player perspective
    let game_key = HashMap::from([
        ("X", "C"),
        ("Y", "A"),
        ("Z", "B")
    ]);
    
    // Mapping of player equivelant of opponent moves
    let identical_move_key = HashMap::from([
        ("A", "X"),
        ("B", "Y"),
        ("C", "Z")
    ]);
    
    // Mapping of value for moves to be applied to player score
    let move_values = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3),
    ]);

    let win_points = 6;
    let draw_points = 3;

    let mut player_score = 0;
   
    for raw_pair in split_data {

        // Split each data point into a Vector of [opponent_move, player_move]
        let pair: Vec<&str> = raw_pair.split(" ").collect::<Vec<&str>>();

        let opponent_move = pair[0];
        let required_result = pair[1];

        // Player needs to lose
        if required_result == "X" {

            // Search for a losing move
            for try_move in ["X", "Y", "Z"] {
                
                // If the opponents move is not the relative identical player move being attempted
                // And the attempted player move is not a winning move
                if identical_move_key[opponent_move] != try_move && game_key[try_move] != opponent_move {
                    player_score += move_values[try_move];
                    break;
                }
            }
        }
        
        // Player needs to draw
        else if required_result == "Y" {
            let player_move = identical_move_key[opponent_move];
            player_score += move_values[player_move];
            player_score += draw_points;
        }

        // Player needs to win
        else {
            for try_move in ["X", "Y", "Z"] {
                if game_key[try_move] == opponent_move{
                    player_score += move_values[try_move];
                    player_score += win_points;
                    break;
                }
            }
        } 
    }

    println!("{}", player_score);
}

fn main() {
    let input = read_input_data();

    let split_data: Vec<&str> = input.split("\r\n").collect::<Vec<&str>>();

    part_one(&split_data);
    part_two(&split_data);
}
