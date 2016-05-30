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
    
    var facts: NSMutableArray = ["Bugger hyphen elements casual on Saturdays at breakfast", "Window things tremendous running caltrops instigating genuineness sideways", "Five words in the mix of Pluto wetting the towel with apple juice heaven joker.", "That yogurt in melanin helpers California jazz ellipsis.", "Modal dope spelunking on a Wednesday afternoon bravely hunting the orange oxen in tudor houses."]

    func getRandomFact() -> String {
        let randomNumber = GKRandomSource.sharedRandom().nextIntWithUpperBound(facts.count)
        
        return facts[randomNumber] as! String
    }
    
}

