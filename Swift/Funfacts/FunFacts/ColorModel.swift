//
//  colorModel.swift
//  FunFacts
//
//  Created by Stephanie Weber on 2/12/16.
//  Copyright © 2016 Stephanie Weber. All rights reserved.
//

import UIKit
import GameKit

struct ColorModel {
    let colorPicker = [
        UIColor(red: 90/255.0, green: 187/255.0, blue: 181/255.0, alpha: 1.0), //teal color
        UIColor(red: 255/255.0, green: 51/255.0, blue: 53/255.0, alpha: 1.0), //pink color
        UIColor(red: 255/255.0, green: 153/255.0, blue: 51/255.0, alpha: 1.0), //light orange color
        UIColor(red: 255/255.0, green: 153/255.0, blue: 255/255.0, alpha: 1.0), //light pink color
        UIColor(red: 255/255.0, green: 255/255.0, blue: 103/255.0, alpha: 1.0), //yellow color
        UIColor(red: 192/255.0, green: 187/255.0, blue: 192/255.0, alpha: 1.0), //light green color
    ]
    func getRandomColor() -> UIColor {
        
        let randomNumber = GKRandomSource.sharedRandom().nextIntWithUpperBound(colorPicker.count)
        return colorPicker[randomNumber]
    }
    
}