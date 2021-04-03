import Foundation




//카카오 1번
func solution(_ gift_cards:[Int], _ wants:[Int]) -> Int {
    var modifiedGiftCard = gift_cards
    var modifiedWants = wants

    for i in modifiedGiftCard {

        if modifiedWants.contains(i), let idx1 = modifiedGiftCard.firstIndex(of: i), let idx2 = modifiedWants.firstIndex(of: i) {
            modifiedGiftCard.remove(at: idx1)
            modifiedWants.remove(at: idx2)
        }


}

    return modifiedGiftCard.count

}


//카카오 2번
let needs = [ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ]

var modifiedNeeds: [[Int]] = []
var modifiedSingleNeeds: [Int] = []
var state = 0
var stateArr: [Int] = []
let r = 2
var answer = needs.count

for i in 0..<needs.count {
    var arr: [Int] = []
    for j in 0..<needs[i].count {
        if needs[i][j] == 1 {
            arr.append(j)
            modifiedSingleNeeds.append(j)
        }
    }
    modifiedNeeds.append(arr)
    
}
print(modifiedNeeds)
print(modifiedSingleNeeds.sorted())



for i in 0..<modifiedSingleNeeds.count {
    if i != 0 {
        if modifiedSingleNeeds.sorted()[i] == modifiedSingleNeeds.sorted()[i - 1] {
            state += 1
           
        } else {
            stateArr.append(state)
            state = 0
        }
        print(modifiedSingleNeeds.sorted()[i], modifiedSingleNeeds.sorted()[i - 1])
    }
}
stateArr.append(state)
for i in 0..<stateArr.count {
    stateArr[i] += 1
}
print(stateArr)

for i in 0..<stateArr.count {
    if i < r {
        
    } else {
        answer -= stateArr[i]
    }
}

print(answer)

