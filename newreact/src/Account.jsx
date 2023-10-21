import React from "react";
import { Typography } from "@material-ui/core";
import { useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
} from "@material-ui/core";

import logout from "./Logout.png";
import User from "./user 1.png";
import order from "./order.png";
import Security from "./padlock.png";
import Address from "./location.png";
import Payment from "./credit-card.png";
import Paypal from "./paypal.png";
import Amazone from "./amazon-pay.png";
import gold from "./jewelry1.png";
import craft from "./tailoring.png";
import Boutique from "./boutique.png";
import gift from "./presents.png";
import acc from "./account2.png";
import shop from "./shopping1.png";

export default function Account() {
  const [popupstate, setpopstate] = useState(false);

  const Logout = () => {
    handleclose();
  };

  const handlelogout = () => {
    console.log("HIII");
    setpopstate(true);
    console.log(popupstate);
  };

  const handleclose = () => {
    setpopstate(false);
  };

  return (
    <div id="Outside_mainddiv">
      <div id="Sidebar">
        <Typography id="options">LOGO</Typography>
        <div id="alloptionconatainer">
          <div id="optioncontainer">
            <img id="optionicons" src={order} alt="order"></img>
            <Typography id="options2">your Orders</Typography>
          </div>
          <div id="optioncontainer">
            <img id="optionicons" src={Security} alt="order"></img>
            <Typography id="options2">Login & security</Typography>
          </div>
          <div id="optioncontainer">
            <img id="optionicons" src={Address} alt="order"></img>
            <Typography id="options2">Your Addresses</Typography>
          </div>
          <div id="optioncontainer">
            <img id="optionicons" src={Payment} alt="order"></img>
            <Typography id="options2">Payment options</Typography>
          </div>
          <div id="optioncontainer">
            <img id="optionicons" src={Paypal} alt="order"></img>
            <Typography id="options2">PayPal</Typography>
          </div>
          <div id="optioncontainer">
            <img id="optionicons" src={Amazone} alt="order"></img>
            <Typography id="options2">Amazon Pay balance</Typography>
          </div>
        </div>
      </div>
      <div id="container1">
        <div className="containertask">
          <div id="todocontain">
            <Typography id="Tittle">My Account </Typography>
          </div>
          <div id="logoutdiv">
            <img
              id="IconProfile"
              onClick={handlelogout}
              src={User}
              alt="img2"
            ></img>
          </div>
        </div>
        {/* <div id="test"></div> */}

        <div id="menu">
          <div id="allmenucontainer">
            <div id="menuoptions">
              <img src={gold} id="optionicon2" alt="img"></img>
              <Typography id="description">Gold & Diamond Jewellery</Typography>
              <Typography id="description2">
                Apps and more Content and devices Music settings
              </Typography>
            </div>
            <div id="menuoptions">
              <img id="optionicon2" src={craft} alt="img"></img>
              <Typography id="description">
                Handloom & Handicraft Store
              </Typography>
              <Typography id="description2">
                Advertising preferences Communication preferences SMS alert
                preferences Message center
              </Typography>
            </div>
            <div id="menuoptions">
              <img id="optionicon2" src={Boutique} alt="img"></img>
              <Typography id="description">The Designer Boutique</Typography>
              <Typography id="description2">
                Amazon Pay Bank accounts for refunds Coupons
              </Typography>
            </div>
            <div id="menuoptions">
              <img id="optionicon2" src={gift} alt="img"></img>
              <Typography id="description">
                Gift Boxes, Gift Tags, Greeting Cards
              </Typography>
              <Typography id="description2">
                Apps and more Content and devices Music settings
              </Typography>
            </div>
            <div id="menuoptions">
              <img id="optionicon2" src={acc} alt="img"></img>
              <Typography id="description">Other accounts</Typography>
              <Typography id="description2">
                Apps and more Content and devices Music settings
              </Typography>
            </div>
            <div id="menuoptions">
              <img id="optionicon2" src={shop} alt="order"></img>
              <Typography id="description">
                Shopping programs and rentals
              </Typography>
              <Typography id="description2">
                Apps and more Content and devices Music settings
              </Typography>
            </div>
          </div>
        </div>

        <Dialog
          open={popupstate}
          onClose={handleclose}
          PaperProps={{ id: "hiddendivcontainer" }}
        >
          <DialogContent id="Dialogger">
            <DialogTitle id="ProfileDialog">
              <Typography className="Typographyusername">user</Typography>{" "}
              <hr id="Line"></hr>
              <DialogActions id="ProfileDialogActions">
                <img
                  id="Logoutpng"
                  src={logout}
                  onClick={Logout}
                  alt="logout"
                />
              </DialogActions>
            </DialogTitle>
          </DialogContent>
        </Dialog>
      </div>
    </div>
  );
}
