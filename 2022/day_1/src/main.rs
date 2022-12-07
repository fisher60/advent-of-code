use std::fs;

fn read_input_data() -> String {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    return data;
}

fn main() {

    // Array to contain the top three calorie values for elves
    let mut top_three: [i64; 3] = [0, 0, 0];

    let input = read_input_data();

    // Split the input into groups of calories belonging to individual elves
    let split_inp = input.split("\r\n\r\n").collect::<Vec<&str>>();
    
    for calories in split_inp.iter() {
        // Split the entire group of calories belonging to one elf
        let split_cals = calories.split("\r\n").collect::<Vec<&str>>();
        
        // convert string representations of calories to i64
        let int_cals: Vec<i64> = split_cals.iter().map(|x| x.parse::<i64>().unwrap()).collect();
        
        let this_sum: i64 = int_cals.iter().sum();

        // Iterate over the current highest values in the top three array
        // If a new high value is found, shift each value to the right in the array starting at the replaced value, then replace the value with the new high
        // This allows us to maintian current highest numbers and also add new highs
        for ind in 0..3 {
            if this_sum > top_three[ind]{
                for slc_ind in ind..3{
                    if slc_ind < 2{
                        top_three[slc_ind + 1] = top_three[slc_ind];
                    }
                }
                top_three[ind] = this_sum;
                break;
            }
        }
        
    }

    let top_three_sum: i64 = top_three.iter().sum();
    println!("{:?}", top_three);
    println!("{}", top_three_sum);

}