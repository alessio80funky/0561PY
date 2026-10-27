  const users = [
            {name: "user1", pass:"pass1", active: true},
            {name: "user2", pass:"pass2", active: false}
        ]

        document.getElementById("login").addEventListener("click", function(){
            const u = document.getElementById("user").value;
            const p = document.getElementById("pass").value;
            const r = document.getElementById("res");

            const usr = users.find(x => x.name === u );

            if(!usr){
                r.textContent = "ユーザーが存在しない"
                r.className = "err";
                return;
            }

            if(!usr.active){
                r.textContent = "ユーザーが無効です";
                r.className = "deactive";
                return;
            }

            if(usr.pass === p){
                r.textContent = "ログイン成功";
                r.className = "ok";
            }else{
                r.textContent = "パスワードが違います";
                r.className = "err";
            }

        })
