<?php

use App\Http\Controllers\FormController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;


/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
*/

Route::middleware('auth:api')->get('/ClientArea', function (Request $request) {
return $request->user();
});

Route::middleware('auth:api')->post('/ClientArea', function (Request $request) {
return $request->user();
});

Route::get('/users', function () {
return response(['opa']);
})->middleware('auth');

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
return $request->user();
});
Route::apiResource('form', FormController::class)->only(['store', 'update']);
