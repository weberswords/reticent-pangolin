//
//  ViewController.swift
//  FunFacts
//
//  Created by Stephanie Weber on 2/11/16.
//  Copyright © 2016 Stephanie Weber. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    
    @IBOutlet weak var addFact: UIBarButtonItem!
    @IBOutlet weak var funFactLabel: UILabel!
    @IBOutlet weak var FunFactButton: UIButton!
    
    
    var factModel = FactModel()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        funFactLabel.text = factModel.getRandomFact()
        }

    override func didReceiveMemoryWarning(){
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func funFactButton() {
        let randomColor = ColorModel().getRandomColor()
        view.backgroundColor = randomColor
        FunFactButton.tintColor = randomColor
        funFactLabel.text = factModel.getRandomFact()
        
    }
}