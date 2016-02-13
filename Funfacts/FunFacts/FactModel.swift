//
//  FactModel.swift
//  FunFacts
//
//  Created by Stephanie Weber on 2/11/16.
//  Copyright © 2016 Stephanie Weber. All rights reserved.
//
import Foundation
import GameKit


struct FactModel {
    
    var facts: NSMutableArray = ["name", "things", "words", "yo", "dope"]

    func getRandomFact() -> String {
        let randomNumber = GKRandomSource.sharedRandom().nextIntWithUpperBound(facts.count)
        
        return facts[randomNumber] as! String
    }
    
}

