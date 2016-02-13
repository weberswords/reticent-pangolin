//
//  addFactViewController.swift
//  FunFacts
//
//  Created by Stephanie Weber on 2/11/16.
//  Copyright © 2016 Stephanie Weber. All rights reserved.
//

import UIKit


var factModel = FactModel()
var facts = factModel.facts

class addFactViewController: UIViewController {
    
    @IBOutlet weak var newFactText: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    override func didReceiveMemoryWarning(){
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func addFact(sender: UIButton) {
        let newFact = newFactText.text
        if newFact == "" {
            print("Error enter text")
        }
        else {
            facts.addObject(newFact!)
            
        }
        print(facts)
    }
    
}