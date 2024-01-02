import React from "react";
import axios from 'axios';
import { useEffect, useState } from 'react';

// import { Typography } from "@material-ui/core";
// import { useState } from "react";
// import {
//   Dialog,
//   DialogTitle,
//   DialogContent,
//   DialogActions,
// } from "@material-ui/core";

// import logout from "./Public/Logout.png";
// import User from "./user 1.png";

// import order from "./Public/order.png";
// import Security from "./Public/padlock.png";
// import Address from "./Public/location.png";
// import Payment from "./Public/credit-card.png";
// import Paypal from "./Public/paypal.png";
// import Amazone from "./Public/amazon-pay.png";

import Fashion from "./Public/fashion.jpg";
import Handloom from "./Public/Handloom.jpg";
import other_account from "./Public/Other-acc.jpg";
import shop from "./Public/Shop.jpg";
import gift from "./Public/Gift.jpg";
import Jewelry from "./Public/Jewelry.jpg";

// import Test from "./Test.jsx";

import Appbar from "./Appbar.jsx";

import Card from "./Card.jsx";
import Grid from "./Grid.jsx";

export default function Account() {


  const [userData, setUserData] = useState([]);

    useEffect(() => {
      // Fetch data from Django API endpoint using Axios
      axios.get('http://127.0.0.1:8000/') // Adjust the URL based on your Django API endpoint
          .then(response => {
              setUserData(response.data.user_data);
          })
          .catch(error => {
              console.error('Error fetching user data:', error);
          });
  }, []);

  console.log("X", userData);
  
  return (
    <div id="Outside_mainddiv">
      {/* <div id="Sidebar">
        <div className="optioncontainer" onClick={click}>
          <Typography id="options">Home</Typography>
        </div>
        <div id="alloptionconatainer">
          <div className="optioncontainer">
            <img id="optionicons" src={order} alt="order"></img>
            <Typography id="options2">your Orders</Typography>
          </div>
          <div className="optioncontainer">
            <img id="optionicons" src={Security} alt="order"></img>
            <Typography id="options2">Login & security</Typography>
          </div>
          <div className="optioncontainer">
            <img id="optionicons" src={Address} alt="order"></img>
            <Typography id="options2">Your Addresses</Typography>
          </div>
          <div className="optioncontainer">
            <img id="optionicons" src={Payment} alt="order"></img>
            <Typography id="options2">Payment options</Typography>
          </div>
          <div className="optioncontainer">
            <img id="optionicons" src={Paypal} alt="order"></img>
            <Typography id="options2">PayPal</Typography>
          </div>
          <div className="optioncontainer">
            <img id="optionicons" src={Amazone} alt="order"></img>
            <Typography id="options2">Amazon Pay balance</Typography>
          </div>
        </div>
      </div> */}
      <div id="container1">
        <Appbar />

        {<Grid id="Grid"
            Item={
              <Card
                image={Jewelry}
                Tittle={"Gold & Diamond Jewellery"}
                Description={"Apps and more, Content and devices, Music settings"}
              />
            }
            Item2={
              <Card
                image={Handloom}
                Tittle={"Handloom & Handicraft Store"}
                Description={"Advertising preferences, Communication preferences, SMS alert preferences, Message center"}
              />
            }
            Item3={
              <Card
                image={Fashion}
                Tittle={"The Designer Boutique"}
                Description={"Amazon Pay, Bank accounts for refunds, Coupons"}
              />
            }
      
            Item4={
              <Card
                image={gift}
                Tittle={"Gift Boxes, Gift Tags, Greeting Cards"}
                Description={"Leave delivery feedback, Lists, Photo Id proofs, Profile "}
              />
            }
            Item5={
              <Card
                image={other_account}
                Tittle={"Other accounts"}
                Description={"Amazon Business registration, seller account, Amazzone Web Services, Login With Amazon "}
              />
            }
            Item6={
              <Card
                image={shop}
                Tittle={"Shopping programs and rentals"}
                Description={"Subscribe & Save"}
              />
            }
          />
        }

      </div>
    </div>
  );
}
