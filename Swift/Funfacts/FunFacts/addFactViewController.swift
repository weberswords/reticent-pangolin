//
//  addFactViewController.swift
//  FunFacts
//
//  Created by Stephanie Weber on 2/11/16.
//  Copyright © 2016 Stephanie Weber. All rights reserved.
//

import UIKit


class addFactViewController: UIViewController {
    
    @IBOutlet weak var newFactText: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
//        funFactLabel.text = factModel.getRandomFact()
    }
    
    override func didReceiveMemoryWarning(){
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        let DestViewController: ViewController = segue.destinationViewController as! ViewController
            DestViewController.newFact = newFactText.text!
            }
    
    @IBAction func addFact(sender: UIButton) {
//        
    }

}