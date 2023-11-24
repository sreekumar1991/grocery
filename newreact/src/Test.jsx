import React from "react";
import MenuItem from "@mui/material/MenuItem";
import { Typography } from "@material-ui/core";
import Menu from "@mui/material/Menu";

export default function Test() {
  // const [set, setvar] = useState(false);

  // const handleClose = () => {
  //   setvar(true);
  // };

  return (
    <div>
      <Menu>
        <MenuItem>
          <Typography textAlign="center">1</Typography>
          <Typography textAlign="center">2</Typography>{" "}
          <Typography textAlign="center">3</Typography>{" "}
        </MenuItem>
      </Menu>
    </div>
  );
}
