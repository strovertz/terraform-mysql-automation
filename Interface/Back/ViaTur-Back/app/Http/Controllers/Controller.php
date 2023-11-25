<?php

namespace App\Http\Controllers;

use App\Models\Form;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller;


class FormController extends Controller
{
    public function update(Request $request)
    {
        $form = new Form($request->only(['email', 'msg', 'phone', 'name']));
        $insert = $form->save();

        if ($insert) {
            return response(status: 200);
        } else {
            return response(status: 500);
        }
    }
    public function store(Request $request)
    {
        $form = new Form($request->only(['email', 'msg', 'phone', 'name']));
        $insert = $form->save();

        if ($insert) {
            return response('deu certo','200');
        } else {
            return response(status: 500);
        }
    }
}
